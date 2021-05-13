listlen, rensuu = map(int, input().split())
listnum = list(map(int, input().split()))
count = 0
count += (listlen - 1) // (rensuu - 1)
count += 1 if (listlen - 1) % (rensuu - 1) > 0 else 0
print(count)
