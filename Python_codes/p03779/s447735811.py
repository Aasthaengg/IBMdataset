X=int(input())

number=0
for n in range(1,pow(10,8)):
    number+=n
    if number>=X:
        break
print(n)
