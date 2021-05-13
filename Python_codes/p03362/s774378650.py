N = int(input())
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
ans = ["11"]
ans_len = 1
counter = 5
A = 55556
for i in range(31, A, 2):
    if ans_len == N:
        break
    if counter == 5:
        if all(i % j != 0 for j in prime):
            ans_len += 1
            ans.append(str(i))
        counter = 0
    prime.append(i)
    counter += 1

print(" ".join(ans))
