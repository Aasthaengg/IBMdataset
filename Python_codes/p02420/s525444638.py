from collections import deque

def shuffle(target, num):
    que = deque(list(target))
    [que.append(que.popleft()) for _ in range(int(num))]
    return "".join(que)

text = input()
while True:
    if text == "-": break
    count = input()
    for _ in range(int(count)):
        n = input()
        text = shuffle(text, n)
    print(text)
    text = input()
