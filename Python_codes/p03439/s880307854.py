import sys

N = int(sys.stdin.readline())

l = 0
r = N - 1

p = 0
print(p, flush=True)
first = sys.stdin.readline().strip()
if first == "Vacant":
    sys.exit()
if first == "Male":
    second = "Female"
else:
    second = "Male"

while True:
    p = (l + r) // 2
    print(p, flush=True)
    sex = sys.stdin.readline().strip()
    if sex == "Vacant":
        # print("end!")
        sys.exit()
    if p % 2 == 0:
        # pまでの間に空席がない場合は性別が同じ
        if sex == first:
            l = p + 1
        # ずれているので、そこまでに空席がある
        else:
            r = p
    else:
        if sex == second:
            l = p + 1
        else:
            r = p