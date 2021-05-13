"""Boot-camp-for-Beginners_Easy013_A_Candy-Distribution-Again_30-August-2020.py"""

A, B, C = map(int, input().split())
a, b, c = A, B, C
i = 0
while True:
    if (A % 2 == 0 and B % 2 == 0 and C % 2 == 0):
        i += 1
        a, b, c = A, B, C
        A = (b+c)/2
        B = (c+a)/2
        C = (a+b)/2
        #print(A,B,C)
        if(A == a and B == b and C == c):
            print(-1)
            break
    else:
        print(i)
        break
