import math

def RotationMatrix(theta):
    '''
    theta in degree
    '''
    c = math.cos(theta*math.pi/180)
    s = math.sin(theta*math.pi/180)
    mat = [[c,-s],[s,c]]
    return mat

def Rotate60(vec):
    mat = RotationMatrix(60)
    result_vec = []
    result_vec.append(mat[0][0]*vec[0] + mat[0][1]*vec[1])
    result_vec.append(mat[1][0]*vec[0] + mat[1][1]*vec[1])
    return result_vec

def get_points(a_vec,b_vec):
    s_vec = [(2*a+b)/3 for (a,b) in zip(a_vec, b_vec)]
    t_vec = [(a+2*b)/3 for (a,b) in zip(a_vec, b_vec)]
    u_vec = [(b-a)/3 for (a,b) in zip(a_vec,b_vec)]
    u_vec = Rotate60(u_vec)
    u_vec = [s+u for (s,u) in zip(s_vec,u_vec)]
    return s_vec, t_vec, u_vec

def get_koch(A, n,cnt, a_vec,b_vec):
    if cnt >= n:
        return
    else:
        cnt += 1
        s_vec, t_vec, u_vec = get_points(a_vec,b_vec)
        get_koch(A, n,cnt, a_vec, s_vec)
        A.append(s_vec)
        get_koch(A, n,cnt, s_vec, u_vec)
        A.append(u_vec)
        get_koch(A, n,cnt, u_vec, t_vec)
        A.append(t_vec)
        get_koch(A, n,cnt, t_vec, b_vec)
        
        
n = int(input())
cnt = 0
a_vec = [0,0]
b_vec = [100,0]
A = []
A.append(a_vec)
get_koch(A, n,cnt, a_vec,b_vec)
A.append(b_vec)
for a in A:
    print(*a)
