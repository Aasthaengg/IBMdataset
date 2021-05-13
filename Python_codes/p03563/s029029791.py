R,G=int(input()),int(input())
for i in range(-4500,4501):
    if int(R+i)==G:
        print(i+G)
        break