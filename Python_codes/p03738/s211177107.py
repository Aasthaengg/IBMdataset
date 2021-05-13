a = input()
b = input()

if len(a)==len(b):
    for i in range(len(a)):
        if a[i]>b[i]:
            print("GREATER")
            quit()
        elif a[i]<b[i]:
            print("LESS")
            quit()
            
elif len(a)>len(b):
    print("GREATER")
    quit()
else:
    print("LESS")
    quit()

print("EQUAL")