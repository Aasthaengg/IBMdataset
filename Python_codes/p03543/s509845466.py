def main():
    N = int(input())

    nums = ['-1']
    res = 'No'

    for num in str(N):
        if nums[0] == num:
            nums.append(num)
            if len(nums) == 3:
                res = 'Yes'
                break
        else:
            nums = [num]
    
    print(res)

if __name__ == '__main__':
    main()