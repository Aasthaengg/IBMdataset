'''
A. train
'''

def main():
    s = [int(x) for x in input().strip().split()]
    return(s[0]-s[1]+1)

print(main())