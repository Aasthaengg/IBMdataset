#%%
import sys
def input():
    return sys.stdin.readline().rstrip()

def main():
    N=int(input())
    
    print(N//2 if N%2 else N//2 - 1)


#%%
if __name__ == '__main__':
    main()

# %%
# from atcoder_test import doTest
# doTest("nikkei2019-2-qual","a",main)