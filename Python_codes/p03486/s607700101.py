
a = input()
b = input()

aa = list(a)
bb = list(b)

aa.sort()
bb.sort(reverse=True)


S = "".join(aa)
T = "".join(bb)

if S < T:
    answer = "Yes"
    print(answer)
else:
    answer = "No"
    print(answer)