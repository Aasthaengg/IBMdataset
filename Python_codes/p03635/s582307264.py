
def Solution(a,b):
    return (a-1)*(b-1)

if __name__=="__main__":
    input = raw_input().split(" ")
    print Solution((int)(input[0]), (int)(input[1]))