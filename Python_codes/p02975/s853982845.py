# A - XOR Circle

N = int(input())
a = list(map(int,input().split()))
a.sort()

if a[N-1]==0:
    ans = 'Yes'
elif N%3!=0:
    ans = 'No'
elif a[0]==a[N//3-1] and a[N//3]==a[2*N//3-1] and a[2*N//3]==a[N-1] and a[0]^a[N//3]^a[2*N//3]==0:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)