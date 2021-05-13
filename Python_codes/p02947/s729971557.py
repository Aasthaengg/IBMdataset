N = int(input())

count = 0
dict = {}
for i in range(N):
    s = ''.join(sorted(input()))
    if(s in dict):
        dict[s] += 1
        count += dict[s]
    else:
        dict[s] = 0
print(count)
