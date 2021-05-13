s = list(input())
kouho = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
for i in s:
    kouho.remove(i)
if kouho == []:
    kouho.append(s.pop(-1))
    for i in range(25):
        dum = s.pop(-1)
        for j in range(len(kouho)):
            if dum < kouho[j]:
                s.append(kouho[j])
                print("".join(s))
                exit()
        else:
            kouho.append(dum)
            kouho.sort()
    else:
        print(-1)
    print("".join(s))
else:
    s.append(kouho[0])
    print("".join(s))
