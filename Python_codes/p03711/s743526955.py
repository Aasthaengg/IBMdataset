#Between Two Integers
def ABC_61_A():
    x,y = map(int, input().split())
    list1 = [1,3,5,7,8,10,12]
    list2 = [4,6,9,11]
    list3 = [2]
    
    if list1.count(x) == 1 and list1.count(y) == 1:
        print('Yes')
    elif list2.count(x) == 1 and list2.count(y) == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':

    ABC_61_A()