N = int(input())
A = list(map(int,input().split()))
cnt = [0]*N

for a in A:
    cnt[a-1] += 1
print('\n'.join(map(str,cnt)))
#count()ではTLE

