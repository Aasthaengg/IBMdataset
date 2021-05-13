a, b, c, d = input()
sign = "+-"
for i in range(2):
        for j in range(2):
                for k in range(2):
                        if eval(a+sign[i]+b+sign[j]+c+sign[k]+d) == 7:
                                print(a+sign[i]+b+sign[j]+c+sign[k]+d + "=7")
                                exit()