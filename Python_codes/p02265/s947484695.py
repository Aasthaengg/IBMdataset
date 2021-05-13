from collections import deque

N = int(input())
ans = deque()

while N > 0:
    N -= 1

    tmp = input().split()

    if tmp[0] == "delete":
        # for文だとTLEになる
        # for i in range(len(ans)):
        #     if ans[i] == tmp[1]:
        #         ans.pop(i)
        #         break

        try:
            ans.remove(tmp[1])
        except:
            pass

    elif tmp[0] == "deleteFirst":
        ans.popleft()

    elif tmp[0] == "deleteLast":
        ans.pop()

    else:
        ans.appendleft(tmp[1])

print(*ans)
