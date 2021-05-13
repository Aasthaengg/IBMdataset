# C - X: Yet Another Die Game
def main():
    x = int(input())

    if x%11==0:
        print((x//11)*2)
    elif x%11<=6:
        print((x//11)*2+1)
    else:
        print((x//11)*2+2)
  
        
if __name__ == '__main__':
    main()
