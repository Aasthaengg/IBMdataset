import sys
def flush() : sys.stdout.flush()

def main():
    N = int(input())
    print(0)
    flush()
    sex = input()
    if sex == "Vacant":
        exit()

    even_sex = sex
    def isOK(mid):
        print(mid)
        flush()
        sex = input()
        if sex == "Vacant":
            exit()
        elif mid%2 == 0:
            if even_sex == sex: return True
            else:return False
        else:
            if even_sex != sex: return True
            else: return False
        
    def bin_search():
        l = 0
        r = N
        while l!=r:
            mid = l + (r-l)//2
            if isOK(mid):
                l = mid
            else:
                r = mid
                
    bin_search()

if __name__ == "__main__":
    main()