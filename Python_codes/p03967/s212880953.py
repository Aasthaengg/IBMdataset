S=input()
acc,ans=0,0
for c in S:
    if c=='g':
        if acc > 0:
            ans += 1
            acc -=1
        else:
            acc += 1
    else:
        if acc > 0:
            acc -= 1
        else:
            ans -= 1
            acc +=1
print(ans)
