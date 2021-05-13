import sys
d = [int(input()) for i in range(6)]
 
def check():
    for i in range(5):
        for j in range(5):
            if abs(d[i]-d[j]) > d[5]:
                print(":(")
                sys.exit()
    print("Yay!")
         
check()