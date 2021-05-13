import sys
C11,C12,C13 = map(int, input().split())
C21,C22,C23 = map(int, input().split())
C31,C32,C33 = map(int, input().split())





if (C11+C22==C12+C21) and (C12+C23==C13+C22) and (C21+C32==C22+C31) and (C22+C33==C23+C32):
    print('Yes')
    sys.exit()


print("No")