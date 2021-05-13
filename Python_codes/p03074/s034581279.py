n, k = list(map(int, input().split()))
s = list(input())

start = []
end = []
flag = True

m = 0

for i in range(n):
    if flag and s[i] == "1":
        flag = False
        start.append(i)
    elif not flag and s[i] == "0":
        flag = True
        end.append(i-1)

if len(start) <= 0 or start[0] != 0:
    start = [0] + start
    end = [0] + end

end.append(n-1)

#print(start, end)

if len(end) <= k:
    print(n)
else:
    m = 0
    for i in range(len(end)-k):
        m = max(m, end[i+k] - start[i] + 1)
    print(m)