n,k,c = map(int,input().split())
s = input()
l = [0]*k
r = [0]*k

start = 0
count = 0
while count <= k-1 and start <= n-1:
    if s[start] == "o":
        l[count] = start
        count += 1
        start += 1+c
    else:
        start += 1
# print(l)

start = n-1
count = k-1
while count >= 0 and start >= 0:
    if s[start] == "o":
        r[count] = start
        count -= 1
        start -= 1+c
    else:
        start -= 1
# print(r)

for i in range(k):
    if l[i] == r[i]:
        print(l[i] + 1)