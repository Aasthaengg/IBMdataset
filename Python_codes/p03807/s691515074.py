n = int(input())
a_l = list(map(int, input().split()))
k = len([ i for i in a_l if i%2 != 0])
ans = 'NO'
if k % 2 == 0:
    ans = 'YES'
print(ans)