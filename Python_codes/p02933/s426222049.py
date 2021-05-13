#%%
import sys
def input():
    return sys.stdin.readline().rstrip()

def main():
    a = int(input())
    s = input()

    if a >= 3200:
        print(s)
    else:
        print('red')

# %%
if __name__ == '__main__':
    main()

# %%
# from atcoder_test import doTest
# doTest("abc138","a",main)