def ispalindrome(str): return 'Yes' if str == str[::-1] else 'No'
a=input()
print(ispalindrome(a))