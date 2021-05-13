N = int(input())
DUMMY = -1
B = [DUMMY] + list(map(int, input().split()))

# 右から見ていって正しい位置にある数字が最後に挿入したもの
def last_insert_elem():
    for b,i in zip(reversed(B), reversed(range(len(B)))):
        if b==i:
            return B.pop(i)
    return DUMMY

ans = []
for _ in range(N):
    e = last_insert_elem()
    if e == -1:
        print(-1)
        exit()
        
    ans.append(e)

print(*reversed(ans), sep='\n')