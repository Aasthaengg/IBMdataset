n = int(input())
s = input()
cnt =0

for i in range(n-2):
    cnt += s[i:i+3] == 'ABC'

print(cnt)