class Coodinate (object):
    """Coodinate object
    This class contains infomation about the coodinates.
    Each instance can have up to 3-dimensional(x,y,z) space coodinates.
    
    params
    ------------------------------
    x : int or floot ,default 0
    y : int or floot ,default 0
    z : int or floot ,default 0


    This class have following methods.
    ------------------------------
    distance : Calculate the straight-line distance between 2 points in Euclidean space.
    midpoint : Calculate the midpoint(halfway) between 2 points.
    manhattan_distance : Calculate the distance between 2 points that is sum of the absolute values their Cartesian coordinates.
    """

    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    
    def distance(self,other):
        """Calculate the straight-line distance between 2 points in Euclidean space.

        params
        ----------
        self : Coodinate object
        other : Coodinate object

        return
        ----------
        distance : floot

        """
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        z_diff_sq=(self.z-other.z)**2
        return (x_diff_sq + y_diff_sq +z_diff_sq)**0.5
    

    def midpoint(self,other):
        """Calculate the midpoint(halfway) between 2 points.

        params
        ----------
        self : Coodinate object
        other : Coodinate object

        return
        ----------
        midpoint : tupul
        
        """
        x_midpoint=(self.x+other.x)/2
        y_midpoint=(self.y+other.y)/2
        z_midpoint=(self.z+other.z)/2
        if self.z == other.z ==0 :
            if self.y == other.y==0:
                return(x_midpoint)
            else:
                return(x_midpoint,y_midpoint) 
        return(x_midpoint,y_midpoint,z_midpoint)

    def manhattan_distance(self,other):
        """Calculate the distance between 2 points that is sum of the absolute values their Cartesian coordinates.

        params
        ----------
        self : Coodinate object
        other : Coodinate object

        return
        ----------
        manhattan_distance : floot

        """

        x_diff_abs=abs(self.x - other.x)
        y_diff_abs=abs(self.y - other.y)
        z_diff_abs=abs(self.z - other.z)
        return(x_diff_abs + y_diff_abs + z_diff_abs)




N,M=map(int,input().split())
S=[]
for i in range(N):
    a,b=map(int,input().split())
    S.append(Coodinate(a,b))

C=[]
for j in range(M):
    c,d=map(int,input().split())
    C.append(Coodinate(c,d))

for k in range (N):
    t1=10**9
    t2=-1
    for l in range (M):
        temp=Coodinate.manhattan_distance(S[k],C[l])
        if temp<t1:
            t1=temp
            t2=l+1
    print(t2)