N=int(input())
s=input()
t=input()
count=0
for i in range(N):
    if s[N-i-1:]==t[:i+1]:
        count=i+1
print(N*2-count)