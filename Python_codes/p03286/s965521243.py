from sys import stdin
def main():
    #入力
    readline=stdin.readline
    N=int(readline())

    if N==0:
        print(0)
    else:
        nums=[]
        fugou=1  #+or-
        power=1  #2**0
        total=0
        while total!=N:
            m=N%(power*2)
            if m==total%(power*2):
                nums.append(0)
            else:
                nums.append(1)
            total+=nums[-1]*power*fugou
            fugou*=-1
            power*=2

        nums=nums[::-1]
        for i in range(len(nums)):
            print(nums[i],end="")
        print()
if __name__=="__main__":
    main()