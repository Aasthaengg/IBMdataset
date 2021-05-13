a, b = map(int, input().split())
wa = a + b
sa = a - b
seki = a * b
li = [wa, sa, seki]
li.sort(reverse=True)
print(li[0])