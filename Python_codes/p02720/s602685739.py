def update_queue(n, queue):
    out = queue[n]
    mod10 = out % 10
    if mod10 != 0:
        queue.append(10 * out + mod10 - 1)
    queue.append(10 * out + mod10)
    if mod10 != 9:
        queue.append(10 * out + mod10 + 1)

    return out, queue

N = int(input())
Q = [1,2,3,4,5,6,7,8,9]

for i in range(N):
    out, Q = update_queue(i, Q)

print(out)