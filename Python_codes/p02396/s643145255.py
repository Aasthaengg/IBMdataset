import itertools as itr

if __name__ == '__main__':
    for i in itr.count(1): # i = 1,2,3,...
        num = int(input())
        if num == 0: break
        print("Case {0}: {1}".format(i, num))