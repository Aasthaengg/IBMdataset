for i in range(0, int(input())):
    sidelen = [int(j) for j in input().split(" ")]
    sidelen.sort(reverse=True)
    if(sidelen[0]**2 == sidelen[1]**2 + sidelen[2]**2):
        print("YES")
    else:
        print("NO")