def resolve():
    '''
    code here
    '''
    import string
    abc = string.ascii_lowercase

    S = input()

    
    for item in abc:
        if item not in S:
            print(item)
            break
    else:
        print('None')




if __name__ == "__main__":
    resolve()
