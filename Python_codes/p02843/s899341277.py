X=int(input())
if X>=2000:
    print(1)
    exit()
for i in range(20):
    if 100*i>X:
        continue
    for j in range(20):
        if 100*i+101*j>X:
            continue
        for k in range(20):
            if 100*i+101*j+102*k>X:
                continue
            for m in range(20):
                if 100*i+101*j+102*k+103*m>X:
                    continue
                for n in range(20):
                    if 100*i+101*j+102*k+103*m+104*n>X:
                        continue
                    for p in range(20):
                        if 100*i+101*j+102*k+103*m+104*n+105*p==X:
                            print(1)
                            exit()
else:
    print(0)