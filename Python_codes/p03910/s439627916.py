N = int(input())
li = [i for i in range(1, N + 1)]
acc = 0
index = 0
for i in range(N):
    acc += li[i]
    if acc >= N:
        index = i
        break
garbage = acc - N
for i in range(index + 1):
    if li[i] != garbage:
        print(li[i])
