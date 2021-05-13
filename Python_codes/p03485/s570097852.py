import math

def main():
    nums = [int(x) for x in input().split()]
    ave = sum(nums)/len(nums)
    print(math.ceil(ave))

if __name__=='__main__':
    main()