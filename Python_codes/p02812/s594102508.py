n = int(input())
#k, x = map(int, input().split())
#hl = list(map(int, input().split()))
s = input()
st='ABC'
count=0
for i in range(n-2):
    if s[i:i+3] == st:
        count+=1
print(count)

