l = [int(input()) for i in range(6)]
out = 0
for i in range(4):
    for j in range(5):
        if l[j]-l[i] > l[5]:
            out += 1
if out > 0:
    print(":(")
else:
    print("Yay!")