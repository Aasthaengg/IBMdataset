#-*-coding:utf-8-*-

def main():
    base_array=[]
    similar_array=[]
    odd_num_array=[]
    counter=0
    ans=1
    array_length = int(input())
    base_array=list(map(int,input().split()))
    for i in base_array:
        data = [i-1,i,i+1]
        similar_array.append(data)
    for array in similar_array:
        for i in array:
            if i % 2 !=0:
                counter+=1
        odd_num_array.append(counter)
        counter=0
    for number in odd_num_array:
        ans*=number
    print(3**array_length-ans)

if __name__=="__main__":
    main()