s = input() + 'T'
n = len(s)
x, y = map(int, input().split())
X = [[], [0]]
xy = 0
cnt =0
for i in s:
    if i == 'F':
        cnt += 1
    else:
        X[xy].append(cnt)
        xy = 1 - xy
        cnt = 0

def f(l):
    if len(l) == 0:
        return [0]
    post = [l[0]]
    for i in range(1, len(l)):
        if l[i]:
            pre = sorted(post)
            post = []
            for j in range(len(pre)):
                if j == 0 or pre[j] != pre[j-1]:
                    post.append(pre[j]+l[i])
                    post.append(pre[j]-l[i])
    return post

print('Yes' if x in f(X[0]) and y in f(X[1]) else 'No')
