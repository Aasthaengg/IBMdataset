#%%
import sys
def input():
    return sys.stdin.readline().rstrip()

def main():
    X, A = map(int, input().split())
    print(0) if X < A else print(10)

# %%
if __name__ == '__main__':
    main()

# %%
# from atcoder_test import doTest
# doTest("abc130","a",main)