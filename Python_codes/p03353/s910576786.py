s = input()
k = int(input())
que = []

def insert(t):
    global que
    for i in range(len(que)):
        if t < que[i]:
            que.insert(i, t)
            if len(que) > 5:
                que = que[:5]
            return
        if que[i] == t:
            return
    if len(que) < 5:
        que.append(t)

for i in range(len(s)):
    for j in range(i+1, min(len(s)+1, i+6)):
        t = s[i:j]
        insert(t)

print(que[k-1])


