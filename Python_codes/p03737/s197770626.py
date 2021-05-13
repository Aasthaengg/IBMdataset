#Three-letter acronym
def ABC_59_A():
    s1,s2,s3 = map(str, input().split())
    
    print(s1[0].upper() + s2[0].upper() + s3[0].upper())

if __name__ == '__main__':

    ABC_59_A()