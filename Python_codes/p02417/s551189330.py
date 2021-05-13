s=''
while True:
    try:
        s += input().lower()
    except:
        break

alph = "abcdefghijklmnopqrstuvwxyz"

for a in alph:
    print("{} : {}".format(a, s.count(a)))