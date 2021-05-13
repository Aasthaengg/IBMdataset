def post_pd(t):
    string_list = ''
    for i in t:
        if i == '?':
            string_list = string_list + 'D'
        else:
            string_list = string_list + i
    
    return string_list

if __name__ == '__main__':
    t = input()
    print(post_pd(t))