import math
def Koch(initialx,endx,initialy,endy,repeat):
    if repeat > num:
        return 0
    else:
        if initialx >= endx:
            onex,secondx = abs(endx-initialx) * 2 / 3 + endx,abs(endx-initialx) / 3 + endx
        else:
            onex,secondx = abs(endx-initialx) / 3 + initialx,abs(endx-initialx) * 2 / 3 + initialx
        if initialy <= endy:
            oney,secondy = abs(endy-initialy) / 3 +initialy,abs(endy-initialy) * 2 / 3 + initialy
        else:
            oney,secondy = initialy - abs(endy-initialy) / 3 ,initialy - abs(endy-initialy) * 2 / 3

        if initialy == endy:
            thirdy = math.sqrt(3) / 2 * (secondx-onex) + oney
            thirdx = (onex + secondx) / 2
        else:
            if initialy > endy:
                if initialx > endx:
                    thirdx = initialx
                    thirdy = secondy
                else:
                    thirdx = endx
                    thirdy = oney
            else:
                if initialx > endx:
                    thirdx = endx
                    thirdy = oney
                else:
                    thirdx = initialx
                    thirdy = secondy
        if [round(initialx,8),round(initialy,8)] not in ans:
            ans.append([round(initialx,8),round(initialy,8)])
        #print(initialx,endx,onex,oney,secondx,secondy,thirdx,thirdy)
        Koch(initialx,onex,initialy,oney,repeat+1)
        Koch(onex,thirdx,oney,thirdy,repeat+1)
        Koch(thirdx,secondx,thirdy,secondy,repeat+1)
        Koch(secondx,endx,secondy,endy,repeat+1)
global num
num = int(input())
ans = []
Koch(0,100,0,0,0)
for n in range(len(ans)):
    print("%.8f %.8f" % (ans[n][0],ans[n][1]))
print("100.00000000 0.00000000")