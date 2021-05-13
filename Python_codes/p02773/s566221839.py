n = int(input())
a = {}
for i in range(n):
    s = input()
    if s in a:
        a[s] += 1
    else:
        a[s] = 1
a = sorted(a.items(), key=lambda x: x[1], reverse=True)
max_a = a[0][1]
w = []
for i in range(len(a)):
    if a[i][1] == max_a:
        w.append(a[i][0])
    else:
        break
w = sorted(w)
for i in range(len(w)):
    print(w[i])